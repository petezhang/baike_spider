
class HtmlOutputer(object):
	"""docstring for HtmlOutputer"""
	def __init__(self):
		self.datas=[]

	def collect_datas(self,data):
		if data is None:
			return None
		self.datas.append(data)

	def output_html(self):
		fout=open('output.html','w',encoding='utf-8')

		fout.write('<html>')
		fout.write('<meta charset="UTF-8">')
		fout.write('<body>')
		fout.write('<table>')

		for data in self.datas:
			fout.write('<tr>')
			fout.write('<td>%s</td>' % data['url'])
			fout.write('<td>%s</td>' % data['title'])
			fout.write('<td>%s</td>' % data['summary'])
			fout.write('</tr>')

		fout.write('</table>')
		fout.write('</body>')
		fout.write('</html>')