node {
    def venvDir = "${env.WORKSPACE}/venv"

    stage('Checkout') {
        checkout scm
    }

    stage('Setup VirtualEnv') {
        sh """
            if [ ! -d "${venvDir}" ]; then
                python3 -m venv ${venvDir}
            fi
            source ${venvDir}/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
        """
    }

    stage('Run Data Ingestion') {
        sh """
            source ${venvDir}/bin/activate
            python data-ingestion/stocks/download_daily_prices.py
        """
    }

    stage('Clean Up') {
        echo "Data ingestion job completed."
    }
}