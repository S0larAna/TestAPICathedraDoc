valid_schema_version = {
    "id": "integer($int64)",
    "lastModifiedDate": "string($date-time)",
    "versionNumber": "string",
    "academicYear": "string",
    "umu": "boolean",
    "departmentId": "integer($int64)"
}

valid_schema_department = {
    "id": "integer($int64)",
    "number": "integer($int32)",
    "name": "string",
    "shortName": "string",
    "faculty": {
        "id": "integer($int64)",
        "name": "string",
        "shortName": "string"
    }
}

valid_schema_faculty = {
    "id": "integer($int64)",
    "name": "string",
    "shortName": "string"
}
