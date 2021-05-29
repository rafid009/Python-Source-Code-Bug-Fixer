import numpy as np 

def function(x):

	f6 = 2
	q5 = x
	paths = []
	try:
		if f6 > 0:
			f6 = f6*8
			paths.append(1)
		else:
			q5 = 3-q5
			q5 = 4*2
			paths.append(2)
		if q5 >= 4:
			q5 = q5/4
			q5 = 2*5
			paths.append(3)
		else:
			x = x/6
			q5 = x+q5
			q5 = q5+9
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))