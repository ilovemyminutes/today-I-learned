from torch import nn, optim

optimizer = optim.Adam()
optimizer.step()

# import logging

# print('hi')

# if __name__ == '__main__':
#     print(__name__)
#     logger = logging.getLogger('main')
#     logging.basicConfig(level=logging.DEBUG) # 로깅 레벨 설정
#     logger.setLevel(logging.WARNING) # 왜 안되지

#     steam_handler = logging.FileHandler(
#         'my.log', mode='w', encoding='utf-8'
#     )
#     logger.addHandler(steam_handler)

#     logger.debug('틀렸어')
#     logger.info('확인해')
#     logger.warning('조심해')
#     logger.error('에러났어')
#     logger.critical('망했어')

# else:
#     print(__name__)


# import configparser
# config = configparser.ConfigParser()

# config.read('example.cfg')
# print(config.sections()) # ['SectionOne', 'SectionTwo', 'SectionThree']

# for key in config['SectionTwo']:
#     value = config['SectionTwo'][key] # SectionTwo에 대해 접근
#     print(f'{key}:{value}')

# import  argparse

# parser = argparse.ArgumentParser(
#     description='Sum two integers'
# )

# parser.add_argument(
#     '-a', '--a_value',
#     dest='aa', help='A integer', type=int,
#     required=True
# )

# parser.add_argument(
#     '-b', '--b_value',
#     dest='b', help='B integer', type=int,
#     required=True
# )

# args = parser.parse_args()
# print(args) # NameSpace
# print(args.aa)
# print(args.b)
# print(args.aa + args.b)


# import csv

# buk_chon_ro = []
# header = []
# rownum = 0

# with open('seoul_bukchon_floating_pop.csv', 'r', encoding='CP949') as p_file:
#     csv_data = csv.reader(p_file)
#     for row in csv_data:
#         if rownum == 0:
#             header = row[0]
#         location = row[7]

#         if location.find(u'북촌로') != -1:
#             buk_chon_ro.append(row)

#         rownum += 1

# with open('seoul_bukchon_floating_pop.csv', 'w', encoding='utf8') as s_file:
#     writer = csv.writer(s_file,
#     delimiter='\t', # 불러올 파일의 구분자
#     quotechar="'", # quotation 방법 지정
#     quoting=csv.QUOTE_ALL)
#     writer.writerow(header)
#     for row in buk_chon_ro:
#         writer.writerow(row)
