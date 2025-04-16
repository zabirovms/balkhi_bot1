import psycopg
from config import DB_CONFIG

async def get_connection():
    return await psycopg.AsyncConnection.connect(**DB_CONFIG)

async def search_poems(query, filters=None):
    async with await get_connection() as conn:
        async with conn.cursor() as cur:
            base_query = """
                SELECT book_title, volume_number, section_title, poem_id, first_line, poem_text
                FROM poems
                WHERE search_vector @@ plainto_tsquery('tajik', %s)
            """
            params = [query]
            
            if filters:
                conditions = []
                if filters.get("book_title"):
                    conditions.append("book_title = %s")
                    params.append(filters["book_title"])
                if filters.get("volume_number"):
                    conditions.append("volume_number = %s")
                    params.append(filters["volume_number"])
                if filters.get("section_title"):
                    conditions.append("section_title = %s")
                    params.append(filters["section_title"])
                if conditions:
                    base_query += " AND " + " AND ".join(conditions)
            
            base_query += " LIMIT 50"
            await cur.execute(base_query, params)
            results = await cur.fetchall()
            
            formatted_results = [
                {
                    "book_title": row[0],
                    "volume_number": row[1],
                    "section_title": row[2],
                    "poem_id": row[3],
                    "first_line": row[4],
                    "poem_text": row[5],
                }
                for row in results
            ]
            return formatted_results
