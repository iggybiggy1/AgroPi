import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta

# Create your models here.

SPECIES = [("Abuta", "Abuta"), ("Acacia", "Acacia"), ("Acalypha", "Acalypha"), ("Acer", "Acer"), ("Adenanthos", "Adenanthos"), ("Aerangis", "Aerangis"), ("Agave", "Agave"), ("Aiphanes", "Aiphanes"), ("Albizia", "Albizia"), ("Allium", "Allium"), ("Aloe", "Aloe"), ("Amaranthus", "Amaranthus"), ("Amomum", "Amomum"), ("Angraecum", "Angraecum"), ("Annona", "Annona"), ("Anthurium", "Anthurium"), ("Antirrhinum", "Antirrhinum"), ("Arabis", "Arabis"), ("Arceuthobium", "Arceuthobium"), ("Ardisia", "Ardisia"), ("Aristida", "Aristida"), ("Asparagus", "Asparagus"), ("Astragalus", "Astragalus"), ("Attalea", "Attalea"), ("Baccharis", "Baccharis"), ("Baeckea", "Baeckea"), ("bamboo", "bamboo"), ("Banksia", "Banksia"), ("Banksia ser. Dryandra", "Banksia ser. Dryandra"), ("Begonia", "Begonia"), ("Berberis and Mahonia", "Berberis and Mahonia"), ("Betula", "Betula"), ("transferred Blechnum", "transferred Blechnum"), ("species used in bonsai", "species used in bonsai"), ("Boronia", "Boronia"), ("Brachyscome", "Brachyscome"), ("Bryum", "Bryum"), ("Bulbophyllum", "Bulbophyllum"), ("Caladenia", "Caladenia"), ("Campanula", "Campanula"), ("Canna", "Canna"), ("Cardamine", "Cardamine"), ("Carex", "Carex"), ("Castanopsis", "Castanopsis"), ("Centaurea", "Centaurea"), ("Chamelaucium", "Chamelaucium"), ("Coccothrinax", "Coccothrinax"), ("Coleus", "Coleus"), ("Commelina", "Commelina"), ("Convolvulus", "Convolvulus"), ("Cordia", "Cordia"), ("Corymbia", "Corymbia"), ("Cousinia", "Cousinia"), ("Crepidium", "Crepidium"), ("Crinum", "Crinum"), ("Crotalaria", "Crotalaria"), ("Croton", "Croton"), ("Cryptocarya", "Cryptocarya"), ("Cuscuta", "Cuscuta"), ("cycad by country", "cycad by country"), ("Cyperus", "Cyperus"), ("Dahlia", "Dahlia"), ("Delphinium", "Delphinium"), ("Dendrobium", "Dendrobium"), ("Dendrochilum", "Dendrochilum"), ("Desmodium", "Desmodium"), ("Diospyros", "Diospyros"), ("Taxonomy of Drosera", "Taxonomy of Drosera"), ("Drosera", "Drosera"), ("Durio", "Durio"), ("Elaeocarpus", "Elaeocarpus"), ("Elaphoglossum", "Elaphoglossum"), ("elm", "elm"), ("Encyclia", "Encyclia"), ("Epidendrum", "Epidendrum"), ("Eragrostis", "Eragrostis"), ("Eremophila", "Eremophila"), ("Erica", "Erica"), ("Erigeron", "Erigeron"), ("Erysimum", "Erysimum"), ("Eucalyptus", "Eucalyptus"), ("Eugenia", "Eugenia"), ("Eulophia", "Eulophia"), ("Euphorbia", "Euphorbia"), ("Ficus", "Ficus"), ("Fritillaria", "Fritillaria"), ("Galium", "Galium"), ("Garcinia", "Garcinia"), ("Geranium", "Geranium"), ("Geum", "Geum"), ("Goodenia", "Goodenia"), ("Grevillea", "Grevillea"), ("Grewia", "Grewia"), ("Guzmania", "Guzmania"), ("Habenaria", "Habenaria"), ("hawthorn with yellow fruit", "hawthorn with yellow fruit"), ("Helichrysum", "Helichrysum"), ("Hibbertia", "Hibbertia"), ("Hieracium", "Hieracium"),
           ("Hippeastrum", "Hippeastrum"), ("Hoya", "Hoya"), ("Hypericum", "Hypericum"), ("Hypericum sect. Adenosepalum", "Hypericum sect. Adenosepalum"), ("Ilex", "Ilex"), ("Impatiens", "Impatiens"), ("Inga", "Inga"), ("Ipomoea", "Ipomoea"), ("Iris", "Iris"), ("Isolepis", "Isolepis"), ("Ixora", "Ixora"), ("Jasminum", "Jasminum"), ("Justicia", "Justicia"), ("Lepanthes", "Lepanthes"), ("Licania", "Licania"), ("Lilium", "Lilium"), ("Lithocarpus", "Lithocarpus"), ("Lobelia", "Lobelia"), ("Lonchocarpus", "Lonchocarpus"), ("Masdevallia", "Masdevallia"), ("Maxillaria", "Maxillaria"), ("Melaleuca", "Melaleuca"), ("Miconia", "Miconia"), ("Millettia", "Millettia"), ("Myristica", "Myristica"), ("Narcissus", "Narcissus"), ("Nepenthes", "Nepenthes"), ("Nepenthes by distribution", "Nepenthes by distribution"), ("Nicotiana", "Nicotiana"), ("Oberonia", "Oberonia"), ("Ocotea", "Ocotea"), ("Oenothera", "Oenothera"), ("Omphalodes", "Omphalodes"), ("Ornithogalum", "Ornithogalum"), ("Oxalis", "Oxalis"), ("Pabstiella", "Pabstiella"), ("Taxonomy of Pachypodium", "Taxonomy of Pachypodium"), ("Pandanus", "Pandanus"), ("Panicum", "Panicum"), ("Passiflora", "Passiflora"), ("Pavonia", "Pavonia"), ("Pelargonium", "Pelargonium"), ("Peperomia", "Peperomia"), ("Persea", "Persea"), ("Phacelia", "Phacelia"), ("Philodendron", "Philodendron"), ("Phyllanthus", "Phyllanthus"), ("Pilea", "Pilea"), ("Pinguicula", "Pinguicula"), ("Pinus", "Pinus"), ("Piper", "Piper"), ("Planchonella", "Planchonella"), ("Pleurothallis", "Pleurothallis"), ("Polygala", "Polygala"), ("Potentilla", "Potentilla"), ("Prasophyllum", "Prasophyllum"), ("Primula", "Primula"), ("Protea", "Protea"), ("Prunus", "Prunus"), ("Psychotria", "Psychotria"), ("Ptilotus", "Ptilotus"), ("Pultenaea", "Pultenaea"), ("Quercus", "Quercus"), ("Ranunculus", "Ranunculus"), ("Rhododendron", "Rhododendron"), ("Ribes", "Ribes"), ("Rosa", "Rosa"), ("Rubus", "Rubus"), ("Salix", "Salix"), ("Salvia", "Salvia"), ("Saurauia", "Saurauia"), ("Schefflera", "Schefflera"), ("Scleria", "Scleria"), ("Sedum", "Sedum"), ("Senecio", "Senecio"), ("Shorea", "Shorea"), ("Silene", "Silene"), ("Sisyrinchium", "Sisyrinchium"), ("Solanum", "Solanum"), ("Sorbus", "Sorbus"), ("Sphagnum", "Sphagnum"), ("Sporobolus", "Sporobolus"), ("Stelis", "Stelis"), ("Stylidium", "Stylidium"), ("Symphyotrichum", "Symphyotrichum"), ("Syzygium", "Syzygium"), ("Taeniophyllum", "Taeniophyllum"), ("Terminalia", "Terminalia"), ("Teucrium", "Teucrium"), ("Thelymitra", "Thelymitra"), ("Tillandsia", "Tillandsia"), ("Trisetum", "Trisetum"), ("Utricularia", "Utricularia"), ("Uvaria", "Uvaria"), ("Vanilla", "Vanilla"), ("Verbascum", "Verbascum"), ("Vernonia", "Vernonia"), ("Verticordia", "Verticordia"), ("Viola", "Viola"), ("Wahlenbergia", "Wahlenbergia"), ]


class PlantManager(models.Manager):
    def create_plant(self, name='New Plant', species=None, user=None, best_temperature=None, temperature_margin=None, best_air_humidity=None, air_humidity_margin=None, best_soil_moisture=None, soil_moisture_margin=None, best_light=None, light_margin=None):
        plant = self.create(name=name, species=species, user=user, best_temperature=best_temperature, temperature_margin=temperature_margin, best_air_humidity=best_air_humidity,
                            air_humidity_margin=air_humidity_margin, best_soil_moisture=best_soil_moisture, soil_moisture_margin=soil_moisture_margin, best_light=best_light, light_margin=light_margin)
        if name == 'demo' or 'Aloes':
            time = datetime.now()
            DataPoint.objects.create(
                air_temperature=10, air_humidity=80, UV_index=7, soil_moisture=10, plant=plant, timestamp=time)
            DataPoint.objects.create(
                air_temperature=15, air_humidity=79, UV_index=7.25, soil_moisture=50, plant=plant, timestamp=(time + timedelta(hours=1)))
            DataPoint.objects.create(
                air_temperature=10, air_humidity=78, UV_index=7.5, soil_moisture=15, plant=plant, timestamp=(time + timedelta(hours=2)))
            DataPoint.objects.create(
                air_temperature=15, air_humidity=77, UV_index=7.25, soil_moisture=75, plant=plant, timestamp=(time + timedelta(hours=3)))
            DataPoint.objects.create(
                air_temperature=10, air_humidity=76, UV_index=7, soil_moisture=30, plant=plant, timestamp=(time + timedelta(hours=4)))
        return plant


class Plant(models.Model):
    """
    Plant table with necessary information to keep the plant alive.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    species = models.CharField(choices=SPECIES, max_length=28, null=True)
    name = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    best_temperature = models.FloatField(null=True)
    temperature_margin = models.FloatField(null=True)
    best_air_humidity = models.FloatField(null=True)
    air_humidity_margin = models.FloatField(null=True)
    best_soil_moisture = models.FloatField(null=True)
    soil_moisture_margin = models.FloatField(null=True)
    best_light = models.FloatField(null=True)
    light_margin = models.FloatField(null=True)

    objects = PlantManager()

    def __str__(self) -> str:
        if self.user is not None:
            return f'Plant {self.name} of species {self.species} for user {self.user.username}'
        return f'Plant {self.name} of species {self.species} for user None'


class DataPoint(models.Model):
    """
    Data Point table containing information about a plant in a moment in time (one data point every hour).
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    air_temperature = models.FloatField(
        validators=[MinValueValidator(-50.0), MaxValueValidator(100.0)])
    air_humidity = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    UV_index = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    soil_moisture = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()

    def __str__(self) -> str:
        return f'DataPoint on {self.timestamp} for plant {self.plant.name}'
