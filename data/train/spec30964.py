import numpy as np 

def function(x):

	j6 = x
	m7 = 0
	paths = []
	try:
		if m7 < 8:
			m7 = j6*j6
			paths.append(1)
		else:
			m7 = m7+2
			x = x+0
			paths.append(2)
		if x > 6:
			x = 9/j6
			j6 = x*9
			x = 4*x
			paths.append(3)
		else:
			j6 = j6+j6
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))