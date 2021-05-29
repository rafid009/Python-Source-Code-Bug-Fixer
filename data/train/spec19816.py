import numpy as np 

def function(x):

	m3 = x
	r6 = 8
	paths = []
	try:
		if r6 >= 4:
			x = x*3
			m3 = m3*x
			m3 = 1/1
			paths.append(1)
		else:
			m3 = 7*m3
			x = r6*9
			paths.append(2)
		if m3 <= 7:
			x = 5-9
			m3 = 1-9
			paths.append(3)
		else:
			x = 6-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))