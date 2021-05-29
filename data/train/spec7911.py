import numpy as np 

def function(x):

	u3 = 0
	t3 = 5
	paths = []
	try:
		if u3 >= 1:
			x = 1+5
			paths.append(1)
		else:
			u3 = u3*9
			u3 = u3-9
			x = x-4
			paths.append(2)
		if u3 > 5:
			x = x*8
			paths.append(3)
		else:
			u3 = u3/1
			x = 4+x
			t3 = t3+x
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		u3 = u3**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))