import numpy as np 

def function(x):

	m1 = x
	d4 = x
	paths = []
	try:
		if x > 2:
			d4 = d4/3
			d4 = 8*d4
			paths.append(1)
		else:
			x = 6*5
			paths.append(2)
		if m1 > 5:
			x = x*2
			d4 = 7-d4
			paths.append(3)
		else:
			m1 = m1+x
			m1 = m1/1
			x = x/5
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))