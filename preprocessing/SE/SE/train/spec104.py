import numpy as np 

def function(x):

	p9 = x
	q8 = 2
	paths = []
	try:
		if q8 > 9:
			x = x+9
			paths.append(1)
		else:
			x = 2+6
			paths.append(2)
		if x > 5:
			x = p9/9
			q8 = q8+p9
			x = x+q8
			paths.append(3)
		else:
			x = 0+5
			p9 = x+x
			p9 = x*q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		q8 = q8**0.5
		return q8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))