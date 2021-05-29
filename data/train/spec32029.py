import numpy as np 

def function(x):

	m5 = x
	j9 = 1
	paths = []
	try:
		if j9 > 3:
			m5 = m5+x
			x = x*x
			j9 = j9-m5
			paths.append(1)
		else:
			m5 = m5/9
			j9 = 1-m5
			j9 = j9+3
			paths.append(2)
		if m5 < 8:
			m5 = 1+x
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))