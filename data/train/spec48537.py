import numpy as np 

def function(x):

	f2 = 2
	q2 = x
	paths = []
	try:
		if f2 < 9:
			q2 = f2-q2
			f2 = f2*6
			paths.append(1)
		else:
			q2 = 3-5
			q2 = 5/q2
			q2 = 8/1
			paths.append(2)
		if q2 <= 4:
			q2 = q2+9
			paths.append(3)
		else:
			x = x*9
			f2 = x+f2
			x = x*0
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))