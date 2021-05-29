import numpy as np 

def function(x):

	j6 = x
	m3 = 2
	paths = []
	try:
		if m3 >= 9:
			m3 = 5/m3
			x = m3-4
			x = j6/1
			paths.append(1)
		else:
			m3 = j6-3
			j6 = x/1
			m3 = 0+4
			paths.append(2)
		if j6 >= 5:
			m3 = m3-8
			paths.append(3)
		else:
			j6 = j6+2
			m3 = m3*5
			m3 = 9-m3
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		x = j6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))