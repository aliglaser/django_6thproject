from django.core.management.base import BaseCommand, CommandError
from minerals.models import Mineral

import json


class Command(BaseCommand):
    help = 'Creating data for the mineral catalog'


    def handle(self, *args, **options):
        with open('minerals.json', encoding='utf-8') as file:
            minerals = json.load(file)

        for mineral in minerals:
            Mineral(
                name = mineral['name'],
                image_filename = mineral['image filename'],
                image_caption = mineral['image caption'],
                category = mineral['category'],
                formula = mineral['formula'],
                strunz_classification = mineral['strunz classification'],
                crystal_system = mineral['crystal system'],
                unit_cell = mineral['unit cell'],
                color = mineral['color'],
                crystal_symmetry = mineral['crystal symmetry'],
                cleavage = mineral['cleavage'],
                mohs_scale_hardness = mineral['mohs scale hardness'],
                luster = mineral['luster'],
                streak = mineral['streak'],
                diaphaneity = mineral['diaphaneity'],
                optical_properties = mineral['optical properties'],
                refractive_index = mineral['refractive index'],
                crystal_habit = mineral['crystal habit'],
                specific_gravity = mineral['specific gravity'],
                group = mineral['group']
        ).save()
        self.stdout.write(self.style.SUCCESS(
            'Mineral data has been successfully added!'
        ))
