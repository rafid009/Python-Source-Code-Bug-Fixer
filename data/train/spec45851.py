import numpy as np 

def function(x):

	j3 = x
	m7 = 2
	paths = []
	try:
		if x >= 7:
			j3 = 3+j3
			paths.append(1)
		else:
			j3 = j3+9
			x = 6+x
			paths.append(2)
		if j3 > 2:
			m7 = m7/m7
			paths.append(3)
		else:
			j3 = j3/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))