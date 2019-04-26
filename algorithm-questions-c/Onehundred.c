//有一栋100层的大楼，该种玻璃杯从某一层楼扔下，刚好会碎。   
//现给你两个杯子，问怎样检测出这个杯子的质量，即找到在哪一层楼刚好会碎？ 
unsigned int DroppingCups(unsigned int cups,unsigned int floors){
	unsigned int i,j,k,t,max;
	unsigned int temp[cups + 1][floors + 1];
		for(i = 0;i < floors + 1;++i){
			temp[0][i] = 0;
			temp[1][i] = i;
		}
		for(i = 2;i < cups + 1;++i){
			temp[i][0] = 0;
			temp[i][1] = 1;
		}
		for(i = 2;i < cups + 1;++i){
			for(j = 2;j < cups + 1;++j){
				for(k = 1,max = UNIT_MAX;k < j;++k){
					t = temp[i][j - k] > temp[i - 1][k - 1] ? temp[i][j - k] : temp[i - 1][k - 1];
					if(max > t){
						max = t;
					}
				}
				temp[i][j] = max + 1;
			}
			
		}
	return temp[cups][floors];			
}
