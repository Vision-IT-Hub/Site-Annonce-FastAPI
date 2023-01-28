from ..models.articles import (Articles)


def ArticleSerializer(article):
    data_ = {
        k: article[k] for k in Articles.schema()["required"]
    }
    data_["_id"] = str(article["_id"])

    return data_
