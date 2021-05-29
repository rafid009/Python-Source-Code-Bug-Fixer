import numpy as np 

def function(x):

	m5 = x
	d3 = 8
	x = x
	paths = []
	try:
		if m5 <= 0:
			x = m5*0
			x = x/3
			paths.append(1)
		else:
			d3 = d3+d3
			d3 = d3*2
			m5 = m5-8
			paths.append(2)
		if x >= 2:
			x = x-6
			paths.append(3)
		else:
			d3 = 9-5
			d3 = d3+x
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		d3 = m5**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))