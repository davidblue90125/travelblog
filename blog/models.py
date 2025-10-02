from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

CATEGORY_COUNTRIES = [
    ('afghanistan', 'Afghanistan'),
    ('albania', 'Albania'),
    ('algeria', 'Algeria'),
    ('andorra', 'Andorra'),
    ('angola', 'Angola'),
    ('antigua_deps', 'Antigua & Deps'),
    ('argentina', 'Argentina'),
    ('armenia', 'Armenia'),
    ('australia', 'Australia'),
    ('austria', 'Austria'),
    ('azerbaijan', 'Azerbaijan'),
    ('bahamas', 'Bahamas'),
    ('bahrain', 'Bahrain'),
    ('bangladesh', 'Bangladesh'),
    ('barbados', 'Barbados'),
    ('belarus', 'Belarus'),
    ('belgium', 'Belgium'),
    ('belize', 'Belize'),
    ('benin', 'Benin'),
    ('bhutan', 'Bhutan'),
    ('bolivia', 'Bolivia'),
    ('bosnia_herzegovina', 'Bosnia Herzegovina'),
    ('botswana', 'Botswana'),
    ('brazil', 'Brazil'),
    ('brunei', 'Brunei'),
    ('bulgaria', 'Bulgaria'),
    ('burkina', 'Burkina'),
    ('burundi', 'Burundi'),
    ('cambodia', 'Cambodia'),
    ('cameroon', 'Cameroon'),
    ('canada', 'Canada'),
    ('cape_verde', 'Cape Verde'),
    ('central_african_rep', 'Central African Rep'),
    ('chad', 'Chad'),
    ('chile', 'Chile'),
    ('china', 'China'),
    ('colombia', 'Colombia'),
    ('comoros', 'Comoros'),
    ('congo', 'Congo'),
    ('congo_democratic_rep', 'Congo {Democratic Rep}'),
    ('costa_rica', 'Costa Rica'),
    ('croatia', 'Croatia'),
    ('cuba', 'Cuba'),
    ('cyprus', 'Cyprus'),
    ('czech_republic', 'Czech Republic'),
    ('denmark', 'Denmark'),
    ('djibouti', 'Djibouti'),
    ('dominica', 'Dominica'),
    ('dominican_republic', 'Dominican Republic'),
    ('east_timor', 'East Timor'),
    ('ecuador', 'Ecuador'),
    ('egypt', 'Egypt'),
    ('el_salvador', 'El Salvador'),
    ('equatorial_guinea', 'Equatorial Guinea'),
    ('eritrea', 'Eritrea'),
    ('estonia', 'Estonia'),
    ('ethiopia', 'Ethiopia'),
    ('fiji', 'Fiji'),
    ('finland', 'Finland'),
    ('france', 'France'),
    ('gabon', 'Gabon'),
    ('gambia', 'Gambia'),
    ('georgia', 'Georgia'),
    ('germany', 'Germany'),
    ('ghana', 'Ghana'),
    ('greece', 'Greece'),
    ('grenada', 'Grenada'),
    ('guatemala', 'Guatemala'),
    ('guinea', 'Guinea'),
    ('guinea_bissau', 'Guinea-Bissau'),
    ('guyana', 'Guyana'),
    ('haiti', 'Haiti'),
    ('honduras', 'Honduras'),
    ('hungary', 'Hungary'),
    ('iceland', 'Iceland'),
    ('india', 'India'),
    ('indonesia', 'Indonesia'),
    ('iran', 'Iran'),
    ('iraq', 'Iraq'),
    ('ireland_republic', 'Ireland {Republic}'),
    ('israel', 'Israel'),
    ('italy', 'Italy'),
    ('ivory_coast', 'Ivory Coast'),
    ('jamaica', 'Jamaica'),
    ('japan', 'Japan'),
    ('jordan', 'Jordan'),
    ('kazakhstan', 'Kazakhstan'),
    ('kenya', 'Kenya'),
    ('kiribati', 'Kiribati'),
    ('korea_north', 'Korea North'),
    ('korea_south', 'Korea South'),
    ('kosovo', 'Kosovo'),
    ('kuwait', 'Kuwait'),
    ('kyrgyzstan', 'Kyrgyzstan'),
    ('laos', 'Laos'),
    ('latvia', 'Latvia'),
    ('lebanon', 'Lebanon'),
    ('lesotho', 'Lesotho'),
    ('liberia', 'Liberia'),
    ('libya', 'Libya'),
    ('liechtenstein', 'Liechtenstein'),
    ('lithuania', 'Lithuania'),
    ('luxembourg', 'Luxembourg'),
    ('macedonia', 'Macedonia'),
    ('madagascar', 'Madagascar'),
    ('malawi', 'Malawi'),
    ('malaysia', 'Malaysia'),
    ('maldives', 'Maldives'),
    ('mali', 'Mali'),
    ('malta', 'Malta'),
    ('marshall_islands', 'Marshall Islands'),
    ('mauritania', 'Mauritania'),
    ('mauritius', 'Mauritius'),
    ('mexico', 'Mexico'),
    ('micronesia', 'Micronesia'),
    ('moldova', 'Moldova'),
    ('monaco', 'Monaco'),
    ('mongolia', 'Mongolia'),
    ('montenegro', 'Montenegro'),
    ('morocco', 'Morocco'),
    ('mozambique', 'Mozambique'),
    ('myanmar_burma', 'Myanmar, {Burma}'),
    ('namibia', 'Namibia'),
    ('nauru', 'Nauru'),
    ('nepal', 'Nepal'),
    ('netherlands', 'Netherlands'),
    ('new_zealand', 'New Zealand'),
    ('nicaragua', 'Nicaragua'),
    ('niger', 'Niger'),
    ('nigeria', 'Nigeria'),
    ('norway', 'Norway'),
    ('oman', 'Oman'),
    ('pakistan', 'Pakistan'),
    ('palau', 'Palau'),
    ('panama', 'Panama'),
    ('papua_new_guinea', 'Papua New Guinea'),
    ('paraguay', 'Paraguay'),
    ('peru', 'Peru'),
    ('philippines', 'Philippines'),
    ('poland', 'Poland'),
    ('portugal', 'Portugal'),
    ('qatar', 'Qatar'),
    ('romania', 'Romania'),
    ('russian_federation', 'Russian Federation'),
    ('rwanda', 'Rwanda'),
    ('st_kitts_nevis', 'St Kitts & Nevis'),
    ('st_lucia', 'St Lucia'),
    ('saint_vincent_grenadines', 'Saint Vincent & the Grenadines'),
    ('samoa', 'Samoa'),
    ('san_marino', 'San Marino'),
    ('sao_tome_principe', 'Sao Tome & Principe'),
    ('saudi_arabia', 'Saudi Arabia'),
    ('senegal', 'Senegal'),
    ('serbia', 'Serbia'),
    ('seychelles', 'Seychelles'),
    ('sierra_leone', 'Sierra Leone'),
    ('singapore', 'Singapore'),
    ('slovakia', 'Slovakia'),
    ('slovenia', 'Slovenia'),
    ('solomon_islands', 'Solomon Islands'),
    ('somalia', 'Somalia'),
    ('south_africa', 'South Africa'),
    ('south_sudan', 'South Sudan'),
    ('spain', 'Spain'),
    ('sri_lanka', 'Sri Lanka'),
    ('sudan', 'Sudan'),
    ('suriname', 'Suriname'),
    ('swaziland', 'Swaziland'),
    ('sweden', 'Sweden'),
    ('switzerland', 'Switzerland'),
    ('syria', 'Syria'),
    ('taiwan', 'Taiwan'),
    ('tajikistan', 'Tajikistan'),
    ('tanzania', 'Tanzania'),
    ('thailand', 'Thailand'),
    ('togo', 'Togo'),
    ('tonga', 'Tonga'),
    ('trinidad_tobago', 'Trinidad & Tobago'),
    ('tunisia', 'Tunisia'),
    ('turkey', 'Turkey'),
    ('turkmenistan', 'Turkmenistan'),
    ('tuvalu', 'Tuvalu'),
    ('uganda', 'Uganda'),
    ('ukraine', 'Ukraine'),
    ('united_arab_emirates', 'United Arab Emirates'),
    ('united_kingdom', 'United Kingdom'),
    ('united_states', 'United States'),
    ('uruguay', 'Uruguay'),
    ('uzbekistan', 'Uzbekistan'),
    ('vanuatu', 'Vanuatu'),
    ('vatican_city', 'Vatican City'),
    ('venezuela', 'Venezuela'),
    ('vietnam', 'Vietnam'),
    ('yemen', 'Yemen'),
    ('zambia', 'Zambia'),
    ('zimbabwe', 'Zimbabwe')
]

# Create your models here.
class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User`.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    country = models.CharField(max_length=50, choices=CATEGORY_COUNTRIES, blank=False, null=False, default='other')
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on= models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.title} - {self.country}"

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return f"Comment {self.body} by {self.author}"
    
class Traveller(models.Model):
    """
    Stores additional information about a traveller related to :model:`auth.User`.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='traveller')
    bio = models.TextField(blank=True)
    profile_image = CloudinaryField('image', default='placeholder')
    fav_country = models.CharField(max_length=50, choices=CATEGORY_COUNTRIES, blank=False, default='other')
    wishlist_country = models.CharField(max_length=50, choices=CATEGORY_COUNTRIES, blank=False, default='other')
        
    def __str__(self):
        return f"{self.user.username}'s Profile"