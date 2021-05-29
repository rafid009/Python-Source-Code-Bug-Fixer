import numpy as np 

def function(x):

	q5 = 7
	d8 = 7
	x = 5
	paths = []
	try:
		if x > 2:
			d8 = d8+1
			q5 = q5+q5
			d8 = x-8
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if q5 <= 7:
			q5 = 2*q5
			paths.append(3)
		else:
			x = 4*5
			x = x+9
			x = x/x
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		d8 = d8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))