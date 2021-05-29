import numpy as np 

def function(x):

	m5 = 6
	a1 = x
	paths = []
	try:
		if x < 4:
			m5 = 1+m5
			x = m5/x
			x = x*a1
			paths.append(1)
		else:
			m5 = a1+x
			a1 = a1*9
			paths.append(2)
		if a1 <= 9:
			a1 = a1+a1
			paths.append(3)
		else:
			a1 = x+a1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))