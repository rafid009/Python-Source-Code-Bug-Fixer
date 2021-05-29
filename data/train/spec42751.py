import numpy as np 

def function(x):

	m2 = 6
	j6 = 5
	paths = []
	try:
		if x <= 2:
			x = 8+j6
			j6 = m2*1
			j6 = j6-8
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if m2 < 6:
			x = x/7
			paths.append(3)
		else:
			m2 = m2/m2
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