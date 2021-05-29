import numpy as np 

def function(x):

	q5 = x
	v2 = x
	paths = []
	try:
		if x > 7:
			q5 = q5*2
			v2 = 7-v2
			paths.append(1)
		else:
			q5 = x*5
			x = x+q5
			x = v2+x
			paths.append(2)
		if q5 < 2:
			q5 = 8+0
			q5 = 7-3
			x = v2*x
			paths.append(3)
		else:
			x = 1/2
			v2 = 4+v2
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))