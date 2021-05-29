import numpy as np 

def function(x):

	m2 = 5
	f3 = 9
	paths = []
	try:
		if f3 < 5:
			f3 = f3+m2
			m2 = m2/8
			paths.append(1)
		else:
			x = 7*x
			paths.append(2)
		if m2 <= 8:
			f3 = m2*1
			paths.append(3)
		else:
			x = x-f3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))