import numpy as np 

def function(x):

	v2 = 0
	q3 = x
	paths = []
	try:
		if q3 < 9:
			v2 = 2-v2
			paths.append(1)
		else:
			v2 = v2-8
			q3 = 4+q3
			v2 = 0+q3
			paths.append(2)
		if v2 > 4:
			x = 1-4
			q3 = v2+7
			paths.append(3)
		else:
			v2 = q3/1
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		q3 = v2**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))