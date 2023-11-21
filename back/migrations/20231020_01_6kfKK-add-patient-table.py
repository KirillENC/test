"""
add patient table
"""

from yoyo import step

__depends__ = {'20230627_01_ukntA-create-users-table'}

steps = [
    step('CREATE TABLE public."Patients"("Id" uuid, "Name" character varying, "Surname" character varying, "Patronymic" character varying, "Gender" integer, "Dob" timestamp without time zone, PRIMARY KEY ("Id"));')
]
