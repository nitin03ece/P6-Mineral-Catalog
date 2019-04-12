from django.urls import reverse
from django.test import TestCase, Client
from .models import Mineral
from django.shortcuts import get_object_or_404


# Create your tests here.
class MineralViewTest(TestCase):
    def setUp(self):
        self.mineral_1 = Mineral.objects.create(
            name = "Abelsonite",
            image_filename = "Abelsonite.jpg",
            image_caption = "Abelsonite from the Green River Formation, Uintah County, Utah, US",
            category = "Organic",
            formula = "C<sub>31</sub>H<sub>32</sub>N<sub>4</sub>Ni",
            strunz_classification = "10.CA.20",
            crystal_system = "Triclinic",
            unit_cell = "a = 8.508 Å, b = 11.185 Åc=7.299 Å, α = 90.85°β = 114.1°, γ = 79.99°Z = 1",
            color = "Pink-purple, dark greyish purple, pale purplish red, reddish brown",
            crystal_symmetry = "Space group: P1 or P1Point group: 1 or 1",
            cleavage = "Probable on {111}",
            mohs_scale_hardness = "2–3",
            luster = "Adamantine, sub-metallic",
            streak = "Pink",
            diaphaneity = "Semitransparent",
            optical_properties = "Biaxial",
            group = "Organic Minerals"
        )

        self.mineral_2 = Mineral.objects.create(
            name = "Abernathyite",
            image_filename = "Abernathyite.jpg",
            image_caption = "Pale yellow abernathyite crystals and green heinrichite crystals",
            category = "Arsenate",
            formula = "K(UO<sub>2</sub>)(AsO<sub>4</sub>)·<sub>3</sub>H<sub>2</sub>O",
            strunz_classification = "08.EB.15",
            crystal_system = "Tetragonal",
            unit_cell = "a = 7.176Å, c = 18.126ÅZ = 4",
            color = "Yellow",
            crystal_symmetry = "H-M group: 4/m 2/m 2/mSpace group: P4/ncc",
            cleavage = "Perfect on {001}",
            mohs_scale_hardness = "2–3",
            luster = "Sub-Vitreous, resinous, waxy, greasy",
            streak = "Pale yellow",
            diaphaneity = "Transparent",
            optical_properties = "Uniaxial (-)",
            group = "Arsenates"
        )

    def test_index_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home.html")

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:mineral_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral_1, resp.context['minerals'])
        self.assertIn(self.mineral_2, resp.context['minerals'])
        self.assertTemplateUsed(resp, "mineral/minerals_list.html")
        self.assertContains(resp, self.mineral_1.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:mineral_detail',
            kwargs={'name':self.mineral_1.name}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral_1, resp.context['mineral'])
        self.assertTemplateUsed(resp, "mineral/mineral_detail.html")

    def test_random_mineral_view(self):
        resp = self.client.get(reverse('minerals:random_mineral'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "mineral/random_mineral.html")
