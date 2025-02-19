import numpy as np 

def function(x):

	u3 = 3
	i6 = 4
	paths = []
	try:
		if i6 <= 4:
			i6 = x/4
			i6 = i6/5
			i6 = 2-i6
			paths.append(1)
		else:
			i6 = u3/i6
			i6 = i6/8
			paths.append(2)
		if i6 > 0:
			u3 = 9*u3
			u3 = u3*5
			u3 = 3*u3
			paths.append(3)
		else:
			u3 = 5*2
			i6 = 8*i6
			i6 = i6+i6
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		u3 = i6**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))