import pandas as pd

# Si, esto es una guarraday habria que mejorarlo.
def get_tag(title):
    tags = ''
    title_lower = title.lower()
    if ('senior' in title_lower):
        tags += "Senior "
    if ('lead' in title_lower):
        tags += "Lead "
    if ('research' in title_lower):
        return f"{tags}Research"
    if ('scientist') in title_lower:
        return f"{tags}Data Scientist"
    if ('learning') in title_lower:
        return f"{tags}Machine Learning Engineer"
    if ('anal') in title_lower:
        return f"{tags}Data Analyst"
    if ('data') in title_lower:
        return f"{tags}Data Engineer"
    if ('full stack') in title_lower or ('fullstack') in title_lower or ('full-stack') in title_lower:
        return f"{tags}Fullstack Engineer"
    if ('front') in title_lower or ('front end') in title_lower or ('react') in title_lower or ('angular') in title_lower:
        return f"{tags}Frontend Engineer"
    if ('back') in title_lower or ('back end') in title_lower:
        return f"{tags}Backend Engineer"
    return title


def get_city(city):
    barcelona = ['Sant Cugat del Vallès', 'Mataró', 'Granollers',
                 'Palau-solità i Plegamans', 'Castelldefels', 'Vilanova i la Geltrú','Martorelles','Badalona','El Prat de Llobregat', 
                 'Esplugues de Llobregat','Sabadell' ,'Barberà del Vallès']
    madrid = ['Tres Cantos', 'Pozuelo de Alarcón', 'Alcobendas', 'Getafe',
              'Alcorcón', 'Boadilla del Monte', 'Leganés', 'Las Rozas de Madrid', 'Sevilla La Nueva', 'San Fernando de Henares',
              'San Sebastián de los Reyes']
    if city in barcelona:
        return "Barcelona"
    if city in madrid:
        return "Madrid"
    return city


def merge_csv_data(args):
    df = pd.read_csv('./input/world_data.csv')

    file_to_merge = pd.read_csv(f'./input/{args.filename}.csv')
    file_to_merge['tags'] = file_to_merge['title'].map(get_tag)
    file_to_merge['city'] = file_to_merge['city'].map(get_city)
    df = df.append(file_to_merge)

    df.to_csv('./input/world_data.csv', encoding='utf-8')
    print("DATA MERGED")
