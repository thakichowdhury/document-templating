#! /usr/bin/env python3
import helpers
import document_generator

def setup_templates_dir() -> str:
    template_dir_path: str = helpers.setup_documents_dir('templates')

    document_generator.create_example_template(template_dir_path)

    return template_dir_path

