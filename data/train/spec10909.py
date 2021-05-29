import numpy as np 

def function(x):

	n6 = x
	t4 = x
	paths = []
	try:
		if n6 < 4:
			x = x+t4
			t4 = 5*0
			paths.append(1)
		else:
			x = 7*x
			n6 = 6/t4
			paths.append(2)
		if t4 <= 3:
			t4 = t4*7
			x = x/2
			paths.append(3)
		else:
			n6 = n6-8
			t4 = x/t4
			x = n6+x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		t4 = n6**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))