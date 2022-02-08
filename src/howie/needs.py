"""
Guesses feelings and needs as described by nonviolent communication using huggingface pipelines

    Copyright (C) 2022  Sioan Zohar

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

needs = list(map(str.lower, ["WELL BEING (peace)",
"Sustenance/Health",
"abundance/thriving",
"exercise",
"food, nutrition",
"nourishment",
"rest, sleep",
"shelter",
"sustainability",
"support/help",
"wellness",
"vitality, energy, aliveness",
"Safety/Security",
"comfort",
"confidence",
"emotional safety",
"familiarity",
"order, structure",
"predictability",
"protection from harm",
"stability",
"trust, faith",
"Rest/Recreation/Fun",
"acceptance",
"appreciation",
"gratitude",
"awareness",
"balance",
"beauty",
"ease",
"equanimity",
"humor",
"movement",
"play",
"relaxation",
"rejuvenation",
"simplicity",
"space",
"tranquility",
"wholeness",
#"wonder",
"CONNECTION (love)",
"Love/Caring",
"affection, warmth",
"beauty",
"closeness, touch",
"companionship",
"compassion, kindness",
"intimacy",
"mattering/importance",
"nurturing",
"sexual connection",
"respect, honoring",
"valuing, prizing",
"Empathy/Understanding",
"Awareness, clarity",
"acceptance",
"acknowledgment",
"communication",
"consideration",
"to be heard",
"to be known",
"presence, listening",
"respect, equality",
"receptivity, openness",
"recognition",
"seeing (see/be seen)",
"self-esteem",
"sensitivity",
"Community/Belonging",
"cooperation",
"fellowship",
"generosity",
"inclusion",
"interdependence",
"harmony, peace",
"hospitality, welcoming",
"mutuality, reciprocity",
"partnership, relationship",
"support, solidarity",
"trust, dependability",
"transparency, openness",
"SELF-EXPRESSION (joy)",
"Autonomy/Authenticity",
"choice",
"clarity",
"congruence",
"consistency",
"continuity",
"dignity",
"freedom",
"honesty",
"independence",
"integrity",
"power, empowerment",
"self-responsibility",
"Creativity/Play",
"adventure",
"aliveness",
"discovery",
"initiative",
"innovation",
"inspiration",
"mystery",
"passion",
"spontaneity",
"Meaning/Contribution",
"appreciation",
"gratitude",
"achievement, productivity",
"celebration, mourning",
"challenge",
"efficacy",
"effectiveness",
"excellence",
"feedback",
"growth",
"learning, clarity",
"mystery",
"participation",
"purpose, value",
"self-actualization",
"self-esteem",
"skill, mastery"]))

structured_needs = {'CONNECTION':[
'acceptance',
'affection',
'appreciation',
'belonging',
'cooperation',
'communication',
'closeness',
'community',
'companionship',
'compassion',
'consideration',
'consistency',
'empathy',
'inclusion',
'intimacy',
'love',
'mutuality',
'nurturing',
'respect/self-respect',
'safety',
'security',
'stability',
'support',
'to know and be known',
'to see and be seen',
'to understand and',
'be understood',
'trust',
'warmth'],

'PHYSICAL WELL-BEING':[
'air',
'food',
'movement/exercise',
'rest/sleep',
'sexual expression',
'safety',
'shelter',
'touch',
'water'],
'HONESTY':[
'authenticity',
'integrity',
'presence'],
'PLAY':[
'joy',
'humor'],

'PEACE':[
'beauty',
'communion',
'ease',
'equality',
'harmony',
'inspiration',
'order'],
'AUTONOMY':[
'choice',
'freedom',
'independence',
'space',
'spontaneity'],
'MEANING':[
'awareness',
'celebration of life',
'challenge',
'clarity',
'competence',
'consciousness',
'contribution',
'creativity',
'discovery',
'efficacy',
'effectiveness',
'growth',
'hope',
'learning',
'mourning',
'participation',
'purpose',
'self-expression',
'stimulation',
'to matter',
'understanding']}

