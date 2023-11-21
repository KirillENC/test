from fastapi import APIRouter
from Api.Identity.Api import login
from Api.Patients.Api import getById as patientGetById, list as patientList
from Api.Users.Api import getById as userGetById
from Api.Users.Api import list as userList
from Api.Users.Api import changeActivity as adminChangeUserActivity
from Api.Definition.Api import allRoles, allDoctors
from Api.Profile.Api import getInfo, changePassword
from Api.Records.Api import list, createRecord, getById
from utils import add_route

router = APIRouter()

add_route(router, allRoles)
add_route(router, allDoctors)

add_route(router, login)

add_route(router, getInfo)
add_route(router, changePassword)

add_route(router, userGetById)
add_route(router, userList)
add_route(router, adminChangeUserActivity)

add_route(router, patientGetById)
add_route(router, patientList)

add_route(router, list)
add_route(router, createRecord)
add_route(router, getById)
