import numpy as np 

def function(x):

	m6 = 6
	f1 = 1
	paths = []
	try:
		if m6 > 7:
			f1 = 6/2
			f1 = 5+6
			paths.append(1)
		else:
			x = x/4
			m6 = m6*x
			x = 4/9
			paths.append(2)
		if m6 <= 5:
			m6 = m6-1
			x = x*x
			paths.append(3)
		else:
			f1 = f1-7
			f1 = f1+0
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		f1 = m6**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))