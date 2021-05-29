import numpy as np 

def function(x):

	m3 = x
	d8 = x
	paths = []
	try:
		if x < 9:
			m3 = 7/d8
			d8 = 0+d8
			paths.append(1)
		else:
			d8 = d8/9
			d8 = d8-9
			paths.append(2)
		if d8 > 2:
			d8 = d8+1
			paths.append(3)
		else:
			x = x+x
			m3 = m3+m3
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))