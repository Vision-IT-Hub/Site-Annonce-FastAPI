def country_serializer(country) -> dict:
    return {
        "_id": str(country["_id"]),
        "country_name": country["country_name"],
        "created_at": country["created_at"],
        "slug": country["slug"],
    }
