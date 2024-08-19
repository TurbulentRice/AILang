from core.commands import *
from core.constants import (
    ACTION_CREATE, ACTION_RUN, ACTION_DELETE, ACTION_UPDATE, ACTION_TEST, ACTION_CONVERT, ACTION_BUILD, ACTION_DEPLOY, ACTION_ANALYZE,
    SUBJECT_PROJECT, SUBJECT_SCRIPT, SUBJECT_DEPENDENCIES, SUBJECT_CODE, SUBJECT_FILE, SUBJECT_SERVICE
)

# Define dispatch table
DISPATCH_TABLE = {
    ACTION_CREATE: {
        SUBJECT_PROJECT: create_project
    },
    ACTION_RUN: {
        SUBJECT_SCRIPT: run_script
    },
    ACTION_DELETE: {
        SUBJECT_PROJECT: delete_project
    },
    ACTION_UPDATE: {
        SUBJECT_DEPENDENCIES: update_dependencies
    },
    ACTION_TEST: {
        SUBJECT_CODE: test_code
    },
     ACTION_CONVERT: {
        SUBJECT_FILE: convert_file,
        SUBJECT_CODE: convert_file
    },
    ACTION_BUILD: {
        SUBJECT_PROJECT: build_project
    },
    ACTION_DEPLOY: {
        SUBJECT_SERVICE: deploy_service
    },
    ACTION_ANALYZE: {
        SUBJECT_CODE: analyze_code
    }
}
