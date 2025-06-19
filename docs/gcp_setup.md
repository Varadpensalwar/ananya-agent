# Google Cloud Platform Setup

While you can run ananya locally, this course also provides the option to deploy the LangGraph application to the cloud.
Specifically, we’ll be using Google Cloud Run, a GCP service designed for deploying containerized applications.

If you're new to [GCP](https://cloud.google.com/), you'll need to create an account, which comes with a generous amount of starting credits.

Once your account is set up and you’ve created a project, open a terminal in the root folder of this repository and follow these steps:


1. Authenticate with Google Cloud:

```bash
gcloud auth login
```

2. Set your Google Cloud project:

```bash
gcloud config set project <PROJECT_ID>
``` 

3. Add the necessary permissions:

```bash
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com
gcloud services enable cloudresourcemanager.googleapis.com
gcloud services enable secretmanager.googleapis.com
```

4. Auth docker registry:

```bash
gcloud config set compute/region <LOCATION>
gcloud auth configure-docker <LOCATION>-docker.pkg.dev -q 
```

Location is the region where you want your project to be deployed. In my case, I'm using 'europe-west1'.

5. Create the Docker repository:

```bash
gcloud artifacts repositories create ananya-app --repository-format=docker \
    --location=<LOCATION> --description="Docker repository for ananya, the WhatsApp Agent" \
    --project=<PROJECT_ID>
```

6. Create secrets for Cloud Run:

```bash
echo -n "<put_your_groq_api_key_here>" | gcloud secrets create GROQ_API_KEY \
    --replication-policy="automatic" \
    --data-file=-

echo -n "<put_your_elevenlabs_api_key_here>" | gcloud secrets create ELEVENLABS_API_KEY \
    --replication-policy="automatic" \
    --data-file=-

echo -n "<put_your_elevenlabs_voice_id_here>" | gcloud secrets create ELEVENLABS_VOICE_ID \
    --replication-policy="automatic" \
    --data-file=-

echo -n "<put_your_together_api_key_here>" | gcloud secrets create TOGETHER_API_KEY \
    --replication-policy="automatic" \
    --data-file=-

echo -n "<put_your_qdrant_url_here>" | gcloud secrets create QDRANT_URL \
    --replication-policy="automatic" \
    --data-file=-

echo -n "<put_your_qdrant_api_key_here>" | gcloud secrets create QDRANT_API_KEY \
    --replication-policy="automatic" \
    --data-file=-

echo -n "<put_your_whatsapp_phone_number_id_here>" | gcloud secrets create WHATSAPP_PHONE_NUMBER_ID \
    --replication-policy="automatic" \
    --data-file=-

echo -n "<put_your_whatsapp_token_here>" | gcloud secrets create WHATSAPP_TOKEN \
    --replication-policy="automatic" \
    --data-file=-

echo -n "<put_your_whatsapp_verify_token_here>" | gcloud secrets create WHATSAPP_VERIFY_TOKEN \
    --replication-policy="automatic" \
    --data-file=-
```

7. Add Cloud Run permissions to secrets:

```bash
gcloud projects add-iam-policy-binding <PROJECT_ID> \
  --member="serviceAccount:$(gcloud projects describe $(gcloud config get-value project) --format="value(projectNumber)")-compute@developer.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

---

These are all the steps required to set up your Cloud Run deployment. Once everything is configured, you can deploy it all using the `cloudbuild.yaml` file.

```bash
gcloud builds submit --region=<LOCATION>
```