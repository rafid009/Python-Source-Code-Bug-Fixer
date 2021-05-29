import numpy as np 

def function(x):

	m3 = 1
	o2 = x
	paths = []
	try:
		if x > 5:
			o2 = m3-o2
			paths.append(1)
		else:
			o2 = o2+m3
			o2 = 0-o2
			paths.append(2)
		if x > 4:
			m3 = m3*4
			o2 = 3/o2
			m3 = o2/8
			paths.append(3)
		else:
			o2 = 5/1
			m3 = m3/m3
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))