# Copyright 2016, 2019 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test Factory to make fake objects for testing
"""
# import random
import factory
from factory.fuzzy import FuzzyChoice, FuzzyInteger
from service.models import Inventory,  Condition, RestockLevel
# from service.models import Product


class InventoryFactory(factory.Factory):
    """Creates fake inventory"""

    class Meta:  # pylint: disable=too-few-public-methods
        """Maps factory to data model"""
        model = Inventory

    product_id = factory.Sequence(lambda n: n)
    inventory_id = None
    condition = FuzzyChoice(
        choices=[
            Condition.NEW,
            Condition.OPEN_BOX,
            Condition.USED
        ]
    )
    restock_level = FuzzyChoice(
        choices=[
            RestockLevel.EMPTY,
            RestockLevel.LOW,
            RestockLevel.MODERATE,
            RestockLevel.PLENTY,
        ]
    )
    quantity = FuzzyInteger(10, 5000)
