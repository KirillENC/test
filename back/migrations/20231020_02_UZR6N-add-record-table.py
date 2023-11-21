"""
add record table
"""

from yoyo import step

__depends__ = {'20231020_01_6kfKK-add-patient-table'}

steps = [
    step('CREATE TABLE public."Records"("Id" uuid, "DoctorId" uuid, "PatientId" uuid, "DateTimeStart" timestamp without time zone, PRIMARY KEY ("Id"));')
]
