import re

async def process_search(query, filters=None):
    from .database import search_poems
    
    results = await search_poems(query, filters)
    processed_results = []
    
    for result in results:
        highlighted_text = re.sub(
            re.escape(query),
            lambda match: f"<b>{match.group()}</b>",
            result["poem_text"],
            flags=re.IGNORECASE
        )
        
        lines = result["poem_text"].split("\n")
        search_index = next((i for i, line in enumerate(lines) if query.lower() in line.lower()), None)
        if search_index is not None:
            start = max(0, search_index - 2)
            end = min(len(lines), search_index + 3)
            context = "\n".join(lines[start:end])
        else:
            context = result["poem_text"][:100]
        
        processed_results.append({
            "book_title": result["book_title"],
            "volume_number": result["volume_number"],
            "section_title": result["section_title"],
            "poem_id": result["poem_id"],
            "first_line": result["first_line"],
            "highlighted_text": highlighted_text,
            "context": context
        })
    
    return processed_results
