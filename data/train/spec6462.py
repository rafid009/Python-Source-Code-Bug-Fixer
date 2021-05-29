import numpy as np 

def function(x):

	t7 = 8
	q9 = x
	paths = []
	try:
		if t7 >= 4:
			q9 = 5*2
			q9 = q9/q9
			q9 = 3*0
			paths.append(1)
		else:
			t7 = t7+3
			paths.append(2)
		if x <= 5:
			x = x*1
			q9 = q9+x
			t7 = t7+x
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))