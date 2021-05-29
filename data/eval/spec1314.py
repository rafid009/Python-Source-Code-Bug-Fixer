import numpy as np 

def function(x):

	m1 = x
	q8 = 8
	paths = []
	try:
		if x > 6:
			m1 = 3/m1
			paths.append(1)
		else:
			q8 = q8+4
			x = 6+6
			paths.append(2)
		if m1 <= 4:
			q8 = q8*5
			q8 = q8-0
			x = x/6
			paths.append(3)
		else:
			q8 = q8/6
			x = 9/5
			q8 = 6/7
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		q8 = m1**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))