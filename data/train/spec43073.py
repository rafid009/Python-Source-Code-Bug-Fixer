import numpy as np 

def function(x):

	m7 = 9
	j3 = 8
	paths = []
	try:
		if x < 2:
			m7 = 8/m7
			x = x+x
			paths.append(1)
		else:
			m7 = m7/m7
			paths.append(2)
		if j3 <= 3:
			x = x+3
			j3 = j3+j3
			paths.append(3)
		else:
			j3 = j3*1
			m7 = m7+9
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