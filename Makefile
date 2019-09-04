
TARGET=GldnRatio
TIME=`date "+%Y%m%d%H%M%S"`

run: backup !

!: clean! ${TARGET}.pdf

${TARGET}.pdf: ${TARGET}.dvi
	dvipdfm ${TARGET}.dvi

${TARGET}.dvi:
	uplatex ${TARGET}.tex

tidy!:
	rm -f ${TARGET}.log ${TARGET}.aux ${TARGET}.ntd 

clean!: tidy!
	rm -f ${TARGET}.pdf ${TARGET}.dvi

keep: 
	mkdir keep
	cp ${TARGET}.log ${TARGET}.aux ${TARGET}.ntd ${TARGET}.pdf ${TARGET}.dvi ${TARGET}.tex keep

keep!: 
	rm -R keep
	mkdir keep
	cp ${TARGET}.log ${TARGET}.aux ${TARGET}.ntd ${TARGET}.pdf ${TARGET}.dvi ${TARGET}.tex keep

tsp: 
	mv keep ${TARGET}_${TIME}


mkbackup: 
	mkdir -p ${TARGET}_BackUp

backup: mkbackup keep tsp
	mv ${TARGET}_${TIME} ${TARGET}_BackUp

backup!: mkbackup keep! tsp
	mv ${TARGET}_${TIME} ${TARGET}_BackUp

py:
	./${TARGET}.py > ${TARGET}.tbl

run!: backup! !

