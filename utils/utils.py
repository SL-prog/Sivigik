#This file is part of Sivigik.
#
#Foobar is free software: you can redistribute it and/or modify
#it under the terms of the GNU Affero General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Foobar is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Affero General Public License for more details.
#
#You should have received a copy of the GNU Affero General Public License
#along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#-*-coding:utf-8-*-

def add_page_to_sitemap(url):
    file_content =''
    with open('/home/sivigik/Sivigik/public/sitemap.xml', 'r') as file:
        file_content = file.read()

    file_content = file_content.replace('</urlset>', '\n')
    file_content += '<url><loc>' + url + '</loc></url>\n</urlset>'

    with open('/home/sivigik/Sivigik/public/sitemap.xml', 'w') as file:
        file.write(file_content)
