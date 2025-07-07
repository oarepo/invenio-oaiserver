# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016-2022 CERN.
# Copyright (C) 2022 Graz University of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Record field function."""

from .percolator import _delete_percolator, _new_percolator
from .proxies import current_oaiserver


def after_insert_oai_set(mapper, connection, target):
    """Update records on OAISet insertion."""
    current_oaiserver.new_percolator_function(
        spec=target.spec, search_pattern=target.search_pattern
    )


def after_update_oai_set(mapper, connection, target):
    """Update records on OAISet update."""
    current_oaiserver.delete_percolator_function(
        spec=target.spec, search_pattern=target.search_pattern
    )
    current_oaiserver.new_percolator_function(
        spec=target.spec, search_pattern=target.search_pattern
    )


def after_delete_oai_set(mapper, connection, target):
    """Update records on OAISet deletion."""
    current_oaiserver.delete_percolator_function(
        spec=target.spec, search_pattern=target.search_pattern
    )
