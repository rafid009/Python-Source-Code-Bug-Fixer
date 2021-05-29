import numpy as np 

def function(x):

	q4 = 3
	r0 = 6
	paths = []
	try:
		if r0 <= 4:
			x = x-r0
			paths.append(1)
		else:
			r0 = r0*x
			x = q4+2
			paths.append(2)
		if x < 7:
			q4 = q4-5
			q4 = q4/2
			q4 = q4*3
			paths.append(3)
		else:
			x = 5+1
			r0 = 1*8
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		q4 = q4**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))