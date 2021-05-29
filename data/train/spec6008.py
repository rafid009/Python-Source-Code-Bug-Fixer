import numpy as np 

def function(x):

	m4 = x
	x1 = 1
	paths = []
	try:
		if x1 <= 1:
			m4 = m4+2
			paths.append(1)
		else:
			m4 = x*x
			x1 = x1/9
			m4 = 1+m4
			paths.append(2)
		if m4 > 7:
			x1 = 7*0
			x1 = x1*2
			paths.append(3)
		else:
			x1 = x1*7
			x1 = x1-9
			x1 = 8/x
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x = x1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))