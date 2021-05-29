import numpy as np 

def function(x):

	q3 = x
	o2 = 4
	x = x
	paths = []
	try:
		if o2 <= 8:
			o2 = 0*o2
			paths.append(1)
		else:
			x = o2+9
			o2 = o2/3
			x = x*q3
			paths.append(2)
		if o2 <= 5:
			x = 3/2
			paths.append(3)
		else:
			o2 = 7*0
			o2 = o2*3
			q3 = o2+0
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		q3 = q3**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))