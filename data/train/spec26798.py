import numpy as np 

def function(x):

	f6 = x
	m2 = x
	paths = []
	try:
		if f6 > 1:
			x = x-f6
			x = 1-6
			x = 9/5
			paths.append(1)
		else:
			m2 = m2/f6
			x = 8*x
			paths.append(2)
		if f6 >= 4:
			x = m2-2
			m2 = 6+m2
			paths.append(3)
		else:
			m2 = m2*x
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))