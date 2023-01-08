from fastapi import APIRouter, Body
from ..database.queries_country import create_country, delete_country, update_country, get_all_country, \
    get_country_by_id
from ..models.country import Country, City, Sector, ResponseModel, ErrorResponseModel
from fastapi.encoders import jsonable_encoder

router = APIRouter()


# ---------------------[COUNTRY]------------------------------

@router.post("/country/create/", response_description="country data added into the database")
async def create_country_data(country: Country = Body(...)):
    country = jsonable_encoder(country)
    new_country = await create_country(country)
    return ResponseModel(new_country, "country added successfully.")


@router.delete("/country/delete/{id}", response_description="Country data deleted from the database")
async def delete_country_data(id: str):
    deleted_country = await delete_country(id)
    if deleted_country:
        return ResponseModel(
            "Country with ID: {} removed".format(id), "Country deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Country with id {0} doesn't exist".format(id)
    )


@router.put("/country/update/{id}")
async def update_country_data(id: str, req: Country = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_country = await update_country(id, req)
    if updated_country:
        return ResponseModel(
            "Country with ID: {} name update is successful".format(id),
            "Country name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the country data.",
    )


@router.get("/country/all/get/", response_description="Get All Countries")
async def get_all_country_data():
    countries = await get_all_country()
    if countries:
        return ResponseModel(countries, "Countries data retrieved successfully")
    return ResponseModel(countries, "Empty list returned")


@router.get("/country/get/{id}", response_description="Country data retrieved")
async def get_country_by_id_data(id):
    country = await get_country_by_id(id)
    if country:
        return ResponseModel(country, "Country data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Country doesn't exist.")
